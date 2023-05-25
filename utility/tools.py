import time

# function to highlight some elements
def highlight(element):
    """Highlights a Selenium webdriver element"""
    d = element._parent
    def apply_style(s):
        d.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)
    orignal_style = element.get_attribute('style')
    apply_style("border: 4px solid violet")
    if (element.get_attribute("style") != None):
        time.sleep(3)
    apply_style(orignal_style)
