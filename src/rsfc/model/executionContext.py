from rsfc.utils import constants
from rsfc.harvesters import somef_harvester as som
from rsfc.harvesters import github_harvester as gt


class ExecutionContext:
    
    def __init__(self, repo, branch, tag, token, mode):
        self.repo = repo
        self.evaluated_tests = constants.REMOTE_EXEC_TESTS #Debe ser una u otra
        self.somef_data = self.run_somef(branch, tag, token, threshold = 0.8)
        self.gh_data = gt.GithubHarvester(self.repo, branch, tag, token)
        self.sw_name, self.sw_version = self.get_basic_metadata(self.somef_data)
    
    
    def run_somef(self, branch, tag, token, threshold): #Ver como alternar entre repo_url y local_repo (poner una otra en base al valor de mode)
        somef_kwargs = {
            "threshold": threshold,
            "ignore_classifiers": True,
            "repo_url": self.repo,
            "readme_only": False,
            "output": "./rsfc_output/somef_assessment.json",
            "pretty": True
        }

        if branch is not None:
            somef_kwargs["branch"] = branch

        elif tag is not None:
            somef_kwargs["tag"] = tag
            
        somef_data = som.SomefHarvester(somef_kwargs, token)
        
        return somef_data
    
    
    def get_basic_metadata(self, somef_data):
        name = somef_data.get("name", [])
        version = somef_data.get("version", [])
        
        if name:
            name = name[0].get("name", None)
        if version:
            version = version[0].get("result", None)
        
        if name:
            name = name.get("value", None)
        if version:
            version = version.get("tag", None) or version.get("value", None)
            
        return name, version
    
    
    def get_execution_data(self):
        return {
            "somef_data": self.somef_data,
            "gh_data": self.gh_data,
            "repo_url": self.repo,
            "sw_name": self.sw_name,
            "sw_version": self.sw_version
        }
        