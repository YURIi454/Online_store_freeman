from blog.models import Blog


def get_list_blogs(topic_id):
    """ Список блога выбранной темы. """

    return Blog.objects.filter(topic=topic_id)