from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return self.menuitem_set.all()

    def get_parent_ids(self):
        if self.parent:
            return self.parent.get_parent_ids() + [self.parent.id]
        else:
            return []
