import os
from jinja2 import Environment, FileSystemLoader


class RenderHtml:
    def generate_html(self, file, context):
        path = os.path.join(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
            "template",
        )
        file_loader = FileSystemLoader(path)
        env = Environment(loader=file_loader)

        template = env.get_template(file)

        output = template.render(context)
        return output
