from django import template
from ..models import Article
register = template.Library()

@register.inclusion_tag('aside.html')
def amalgamate():
    articles = Article.objects.all()
    dates = Article.objects.dates('pub_date', 'year', order='DESC')
    # 合并分类，并按出现次数排序
    categories = []
    for article in articles:
        cat = str(article.category)
        if cat not in categories:
            categories.append(cat)
    # 提取归档年份
    years = []
    for date in dates:
        year = date.year
        if year not in years:
            years.append(year)
    # 提取文章包含的所有标签，并按出现次数排序
    tags = []
    for article in articles:
        Tags = str(article.tags)
        for tag in Tags.split(','):
            tag = tag.strip();
            if tag not in tags and tag != '':
                tags.append(tag)

    return {'categories': categories, 'years': years, 'tags': tags}
