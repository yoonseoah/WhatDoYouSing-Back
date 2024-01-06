class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
<<<<<<< HEAD
    
    @property
    def current_page(self):
        # 현재 페이지 번호 반환
        if self.paginator is not None and hasattr(self.paginator, 'page'):
            return self.paginator.page.number
        else:
            return None
=======
        
>>>>>>> ae6ca88fd134e09c52d314fce0959a3f24782f00