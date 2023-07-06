"""Module for geo information functions."""
from ip2geotools.databases.noncommercial import DbIpCity


def geo_infos(ip_src_list, ip_dst_list):
    """Gets the longitude and latitude for each IP in the source and destination list."""
    src_geo_info = []
    dst_geo_info = []
    i = 0

    for j in range(len(ip_src_list)):
        try:
          src_response = DbIpCity.get(ip_src_list[j], api_key='free')
          dst_response = DbIpCity.get(ip_dst_list[j], api_key='free')
        except:
          continue
        if src_response.latitude == None or dst_response.latitude == None:
          continue
        i +=1
        src_geo_info.append([src_response.latitude, src_response.longitude, src_response.region])
        dst_geo_info.append([dst_response.latitude, dst_response.longitude, dst_response.region])
        if i == 10:
            break

    return src_geo_info, dst_geo_info
