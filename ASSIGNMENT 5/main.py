from fastapi import FastAPI, Query

app = FastAPI()

products = [
    {"id":1,"name":"Wireless Mouse","price":499,"category":"Electronics"},
    {"id":2,"name":"Notebook","price":99,"category":"Stationery"},
    {"id":3,"name":"USB Hub","price":799,"category":"Electronics"},
    {"id":4,"name":"Pen Set","price":49,"category":"Stationery"}
]
from fastapi import FastAPI, Query

app = FastAPI()

products = [
    {"id":1,"name":"Wireless Mouse","price":499,"category":"Electronics"},
    {"id":2,"name":"Notebook","price":99,"category":"Stationery"},
    {"id":3,"name":"USB Hub","price":799,"category":"Electronics"},
    {"id":4,"name":"Pen Set","price":49,"category":"Stationery"}
]


@app.get("/products/search")
def search_products(keyword: str):

    result = [p for p in products if keyword.lower() in p["name"].lower()]

    if not result:
        return {"message": f"No products found for: {keyword}"}

    return {
        "keyword": keyword,
        "total_found": len(result),
        "products": result
    }



@app.get("/products/sort")
def sort_products(
    sort_by:str="price",
    order:str="asc"
):

    if sort_by not in ["price","name"]:
        return {"error":"sort_by must be 'price' or 'name'"}

    reverse=(order=="desc")

    result=sorted(products,key=lambda p:p[sort_by],reverse=reverse)

    return {
        "sort_by":sort_by,
        "order":order,
        "products":result
    }

@app.get("/products/page")
def paginate_products(
    page:int=1,
    limit:int=2
):

    start=(page-1)*limit
    result=products[start:start+limit]

    total_pages=-(-len(products)//limit)

    return {
        "page":page,
        "limit":limit,
        "total_pages":total_pages,
        "products":result
    }

@app.get("/products/page")
def paginate_products(
    page:int=1,
    limit:int=2
):

    start=(page-1)*limit
    result=products[start:start+limit]

    total_pages=-(-len(products)//limit)

    return {
        "page":page,
        "limit":limit,
        "total_pages":total_pages,
        "products":result
    }

@app.get("/products/sort-by-category")
def sort_by_category():

    result = sorted(products, key=lambda p: (p["category"], p["price"]))

    return {
        "products": result,
        "total": len(result)
    }

@app.get("/products/browse")
def browse_products(
    keyword:str|None=None,
    sort_by:str="price",
    order:str="asc",
    page:int=1,
    limit:int=4
):

    result=products

    if keyword:
        result=[p for p in result if keyword.lower() in p["name"].lower()]

    if sort_by in ["price","name"]:
        result=sorted(result,key=lambda p:p[sort_by],reverse=(order=="desc"))

    total=len(result)

    start=(page-1)*limit
    paged=result[start:start+limit]

    return {
        "keyword":keyword,
        "sort_by":sort_by,
        "order":order,
        "page":page,
        "limit":limit,
        "total_found":total,
        "total_pages":-(-total//limit),
        "products":paged
    }