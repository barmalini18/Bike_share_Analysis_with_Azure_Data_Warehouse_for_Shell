from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData

def main():

    graph = create_schema_graph(metadata=MetaData('postgresql://postgres:Unicorn18@localhost/udacityproject'))
    
    graph.write_png('postgres_erd.png')

if __name__ == "__main__":
    main()