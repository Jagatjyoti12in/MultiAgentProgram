from crewai import Agent

agent = Agent(
    role="Tester",
    goal="Say hello",
    backstory="Simple test",
    llm=llm,
    verbose=True
)

print(agent.execute_task("Say hello"))