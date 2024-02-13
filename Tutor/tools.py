from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel

questions = {
    "1a": "At the start of this project you completed a literature review to learn more about indoor films.  Based on your readings, what ‘order of magnitude’ concentrations of nitrite, nitrate, and phosphate do you expect in your samples? Why do you expect that ‘order of magnitude’?",
    "1b": "At the start of this project you completed a literature review to learn more about indoor films. While you’re doing your laboratory work to extract the film and then analyze it on the HPLC, what steps will you take to minimize uncertainty in your analysis?",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
}

rubrics = {
    "1a": "ppm concentration",
    "1b": '''Answers should include 2-3 of the following:
- Quantitatively transfer solutions/salts for solution prep
- Minimize contact with the wafer surface to not accidentally contaminate the surface or remove surface film
- Use clean glassware, filters, syringes as to not contaminate the sample
- Use HPLC grade water and solvents to not introduce additional ions
- Run all standards and samples in triplicate to ensure reliability
''',
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
}

class PreLabReportTools:
    def __init__(self):
        ...

    def get_tools(self):
        return [
            DummyTool(),
        ]
    

#dummy tool for now
class DummyTool(BaseTool): #in case we want to add tools later
    name = "dummy_tool"
    description = "This is a dummy tool. It does nothing. DO not use this tool."

    def _run(self, input):
        return input

