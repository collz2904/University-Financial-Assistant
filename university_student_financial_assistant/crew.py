import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task






@CrewBase
class UniversityStudentFinancialAssistantCrew:
    """UniversityStudentFinancialAssistant crew"""

    
    @agent
    def budget_forecast_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config["budget_forecast_agent"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def savings_investment_advisor_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config["savings_investment_advisor_agent"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def summary_visualization_generator_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config["summary_visualization_generator_agent"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def analyze_budget_and_create_3_month_forecast(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_budget_and_create_3_month_forecast"],
            markdown=False,
            
            
        )
    
    @task
    def generate_savings_and_investment_recommendations(self) -> Task:
        return Task(
            config=self.tasks_config["generate_savings_and_investment_recommendations"],
            markdown=False,
            
            
        )
    
    @task
    def create_final_student_financial_report(self) -> Task:
        return Task(
            config=self.tasks_config["create_final_student_financial_report"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the UniversityStudentFinancialAssistant crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


