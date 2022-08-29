import re
from core.models import MediaConverter


def search_subs(keyword, query_id):
    search_obj = MediaConverter.objects.get(id=query_id)
    subs = search_obj.subtitle
    segment_list = list()
    alloc_seg = list()
    for line in subs.split('\n'):
        temp_seg = re.findall(r"\d{1}\:\d{2}\:\d{2}\,\d{3}", line)
        if temp_seg:
            alloc_seg = temp_seg
        if keyword in " ".join(line.split()):
            segment_list.append(alloc_seg)
    return segment_list


