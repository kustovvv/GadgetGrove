def seller_base(request):
    pages = ['catalog', 'reviews', 'contacts', 'schedule', 'about']
    page_urls = {page: 'seller:seller_' + page for page in pages}
    return {
            'pages': pages,
            'page_urls': page_urls
            }