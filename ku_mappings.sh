curl -XPUT 'localhost:9200/ku?pretty' -H 'Content-Type: application/json' -d
[
    "setting":{
        "number_of_shards": 3,
        "number_of_replace": 0
    },
    "mappings" :{
        "webpage" :{
            "properites":{
                "BaseUrl": {"type" : "keyword"},
                "Url": {"type" :"keyword"},
                "Title": {"type" : "text", "analyzer": "Thai"},
                "Body": {"type" : "text", "analyzer": "Thai"},
                "Encoding" : {"type" :"keyword"},
                "Links" : {"type" :"keyword"}
                "Crawling_date" : {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss"
                }
            }
        }
    }
]