def update_file(remove_list):
    with open("allow_list.txt","r") as a:
        ip_addresses = a.read()
    list_ip_addresses = ip_addresses.split()
    for element in remove_list:
        while element in list_ip_addresses:
            list_ip_addresses.remove(element)

    ip_addresses = "\n".join(list_ip_addresses)
    with open("allow_list_updated.txt","w") as import_file:
        import_file.write(ip_addresses)
    

update_file(["123", "126"])


