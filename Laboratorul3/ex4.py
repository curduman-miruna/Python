def build_xml_element(tag, content, **args):
    #** permite pasarea mai multor argumente sub forma unui dictionar
    xml_element = f"<{tag}"
    for key, value in args.items():
        xml_element += f' {key}="{value}"'
    xml_element += f">{content}"
    xml_element += f"</{tag}>"
    return xml_element

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)
