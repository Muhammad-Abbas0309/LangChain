from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
# loader=PyPDFLoader(r'path')
# text= loader.load()
text="Cricket is a sport that blends skill, strategy, and patience into a game loved by millions around the world. Played between two teams, it revolves around the contest between bat and ball, where every run, wicket, and over can change the course of a match. From the calm concentration of a batsman facing a fast bowler to the electric energy of a packed stadium during a close finish, cricket offers drama in many forms. It teaches teamwork, discipline, and respect for opponents, while also allowing individual brilliance to shine. Whether played on dusty village grounds or in world-class stadiums, cricket remains more than just a game—it is a passion that connects people across cultures and generations."
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_text(text)
print(result)