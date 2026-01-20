from langchain_text_splitters import RecursiveCharacterTextSplitter
text="""Cricket is one of the most popular sports in the world, enjoyed by millions of fans across different countries. It is played between two teams, each consisting of eleven players, and the objective is to score more runs than the opposing team.

The game requires a combination of physical skill, mental strength, and strategic thinking. Batsmen must time their shots carefully, bowlers need precision and variation, and fielders play a crucial role in supporting their team through agility and awareness.

Cricket is played in several formats, including Test matches, One Day Internationals, and Twenty20 games. Each format offers a unique experience, ranging from the patience and endurance required in Test cricket to the fast-paced excitement of T20 matches.

Beyond competition, cricket also brings people together. It creates a sense of unity, passion, and national pride, especially during international tournaments. For many fans, cricket is not just a sport but an emotion shared across generations."""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10

)
result=splitter.split_text(text)
print(result)