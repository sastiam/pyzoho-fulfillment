from collections import OrderedDict


class TextResponse:
    """
    [
        {
            "text": display_text
        }
    ]
    """
    def __init__(self, display_text) -> None:
        self.single_response = OrderedDict()
        self.single_response["text"] = display_text

class ImageResponse:
    """
     [
        {
        "text": display_text,
        "image": display_img
        }
    ]
    """
    def __init__(self, display_text, display_img) -> None:
        self.image_response = OrderedDict()
        self.image_response["text"] = display_text
        self.image_response["image"] = display_img


class SuggestionsChips:
    """
    [
        chip-1,
        chip-2,
        .
        .
        .
        chip-n
    ]
    """
    def __init__(self, suggestion_chips: list) -> None:
        self.suggestions = []
        for item in suggestion_chips:
            self.suggestions.append(item)
            
class Item:
    
    def __init__(self, title:str, subtitle:str, id: str, image: str, linkAction: str) -> None:
        self.item = OrderedDict()
       
        # elements
        self.item["title"] = title
        self.item["subtitle"] = subtitle
        self.item["id"] = id
        self.item["image"] = image
        # actions
        self.actions = []
        actions = dict()
        actions["label"] = "Ver más",
        actions["name"] = "bookbtn",
        actions["type"] = "url",
        actions["link"] = linkAction
        self.actions.append(actions)
        self.item["actions"] = self.actions
        
class CarouselItems:
    
    def __init__(self, text: str) -> None:
        self.caritems = OrderedDict()
        self.elements = []
        self.caritems["type"] = "multiple-product"
        self.caritems["text"] = text
        self.caritems["elements"] = self.elements
    
    def add(self, element):
        if isinstance(element, Item):
            self.elements.append(element.item)


