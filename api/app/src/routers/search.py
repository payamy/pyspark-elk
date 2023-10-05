from elasticsearch import Elasticsearch
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models import User
from ..dependencies import get_current_active_user, get_db
from ..crud.visit import create_visit_record
from ..schemas import VisitCreate


router = APIRouter()
es_node = 'elasticsearch'
es_port = '9200'
es_index = 'artists_words'
es = Elasticsearch(hosts=[f"http://{es_node}:{es_port}"])


@router.get("/top_words")
async def get_words_of_artist(
        artists_name: str,
        user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db),
):
    artists_field = ''.join([f'({artist}) OR ' for artist in artists_name.split(',')])
    print(artists_field)
    resp = es.search(index=es_index, query={"match": {"artist": artists_field}})

    response_obj = {}

    for hit in resp['hits']['hits']:
        response_obj[hit["_source"]["artist"]] = hit["_source"]["top_words"]

    data = {
        "endpoint": "top_words",
        "query": f"artists_name={artists_name}"
    }
    visit = VisitCreate(**data)
    create_visit_record(db, user.id, visit)

    return response_obj
