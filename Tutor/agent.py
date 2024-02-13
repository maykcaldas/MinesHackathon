from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.agents import ZeroShotAgent
from langchain.tools import BaseTool
import os

questions = {
    "1": "Describe how reverse-phase HPLC (RP-HPLC) is different than normal phase HPLC and what chemical problems RP-HPLC would be better suited for",
    "2": "At the start of this project you completed a literature review to learn more about indoor films. While you’re doing your laboratory work to extract the film and then analyze it on the HPLC, what steps will you take to minimize uncertainty in your analysis?",
    "3": "For this separation a reverse-phase silica capped C18 column (catalog number 059148) will be used. This column has a carbon load of 18%. The mobile phase will be 60% acetonitrile/40% water (v:v). For the best separation, the mobile phase must be adjusted to pH = ~2.6 using sulfuric acid.   Using chemistry concepts and principles, why would a low pH around 2.60 beneficial to the separation of nitrate, nitrite, and phosphate? (Think about the analytes of interest and the column composition)",
    "4": "For this separation a reverse-phase silica capped C18 column (catalog number 059148) will be used. This column has a carbon load of 18%. The mobile phase will be 60% acetonitrile/40% water (v:v). For the best separation, the mobile phase must be adjusted to pH = ~2.6 using sulfuric acid. Provide a detailed list of steps here that you will use to prepare your mobile phase.",
    "5": "What species might be present that could be interferents for your measurement of nitrate, nitrite, and phosphate? Why might those species interfere with your measurements?",
}

rubrics = {
    "1": '''- RP-HPLC is different than HPLC in terms of the column choice and mobile phase choice, allowing for the separation of different types of molecules;
    - HPLC uses a polar stationary phase (column) and nonpolar mobile phase so that more polar species will be retained longer on the column and the more nonpolar species will elute sooner with the mobile phase;
    - RP-HPLC uses a nonpolar stationary phase (column) and polar mobile phase so that the more nonpolar species will be retained longer on the column and the more polar species will elute sooner with the mobile phase.
''',
    "2": '''- Quantitatively transfer solutions/salts for solution prep
    - Minimize contact with the wafer surface to not accidentally contaminate the surface or remove surface film;
    - Use clean glassware, filters, syringes as to not contaminate the sample;
    - Use HPLC grade water and solvents to not introduce additional ions;
    - Run all standards and samples in triplicate to ensure reliability.
''',
    "3": '''- A low pH is beneficial for the separation of ions because it allows some of the silanol groups on the C18 column to be protonated, helping to attract and retain the negatively charged ions being analyzed
''',
    "4": '''- To make 1L of mobile phase:
        - Add 600 mL of HPLC grade acetonitrile and dilute volumetric flask to the mark with Millipore water (~400 mL)
        - Cap and invert the volumetric flask to mix the solution
        - Add sulfuric acid dropwise to adjust the pH to ~2.6 using a calibrated pH probe to monitor the pH changes and stirring in between drops  
        - Sonicate the mobile phase for ~5 min to remove any bubbles 
''',
    "5": '''- Other anions of similar structure such as sulfate and phosphate
    - H+ interacting with nitrite to become HONO

''',
}


instructions = PromptTemplate(
    input_variables=["question", "rubric", "answer"],
    template="""You are the Professor of a general chemistry course at a university.

    You are grading a pre-lab report for a student in your class for this following experimental procedure:
    ### Procedure’s Purpose ###
    In this procedure you will quantify nitrate, nitrite, and phosphate* concentrations (ppm) in indoor surface films that you have collected earlier in the semester. You must isolate nitrate, nitrite, and phosphate from the other film components. High performance liquid chromatography, (HPLC) with UV detection will serve as the separation technique.
    *note: you may not be able to isolate phosphate but go ahead and include it as an analyte of interest.
    
    I will give you a pre-lab question and the associated rubric. I will also give you a student's response to the question. Your task is to guide the student correctly answer the pre-lab question based on the rubric.

    Provide a detailed response to the student's answer, feedback on how to improve, and a numeric grade between 0 and 10.
    Do not output any of the rubrics back to the student.
    Do not give the final answer, give feedback to the student and directions on how to improve their answer.
    Do not use any tools. 

    Here is the rubric: {rubric}
    Here is the pre-lab question: {question}
    Here is the student's answer: {answer}
    """)

#dummy tool for now
class DummyTool(BaseTool): #in case we want to add tools later
    name = "dummy_tool"
    description = "This is a dummy tool. It does nothing. DO not use this tool."

    def _run(self, input):
        return input


class PreLabReport:
    def __init__(self, temperature=0, llm='gpt4', questionID=None, answer=None):
        self.temperature = temperature
        self.llm = llm
        self.prompt = instructions
        self.question = questions[questionID]
        self.rubric = rubrics[questionID]
        self.answer = answer

        self.model = ChatOpenAI(
            temperature=self.temperature,
            model="gpt-4",
            client=None,
            streaming=True,
            verbose=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )
        self.tools = [DummyTool()]
        self.agent_instance = AgentExecutor.from_agent_and_tools(
            tools=self.tools,
            agent=ZeroShotAgent.from_llm_and_tools(
                llm=self.model, tools=self.tools
            ),
            handle_parsing_errors=True,
            return_intermediate_steps=False,
            verbose=False
        )
       
    def run(self):
        output = self.agent_instance.invoke(self.prompt.format(question=self.question,
                                                                rubric=self.rubric,
                                                                answer=self.answer))
        return output["output"]

