{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1JNVDj3WXEWJXM7TJAet43hX9gUWxgo_h",
      "authorship_tag": "ABX9TyNsqCtjG02/rGt+uAHo7rRK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BrunoAndrade1/Arquivo/blob/main/Grafico_Bruno_Pyplot.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gSZfHna1u17n"
      },
      "outputs": [],
      "source": [
        "\n",
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from matplotlib import pyplot\n",
        "import plotly.graph_objects as go\n",
        "\n",
        "\n",
        "class Pyplot:\n",
        "    def __init__(self, current_value, min_value, max_value, quadrant_colors, quadrant_text, sensor_text, width=200, height=150):\n",
        "        self.current_value = current_value\n",
        "        self.min_value = min_value\n",
        "        self.max_value = max_value\n",
        "        self.quadrant_colors = quadrant_colors\n",
        "        self.quadrant_text = quadrant_text\n",
        "        self.sensor_text = sensor_text\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "\n",
        "    def Bruno_gauge(self):\n",
        "        n_quadrants = len(self.quadrant_colors) - 1\n",
        "        hand_length = np.sqrt(2) / 4\n",
        "        hand_angle = np.pi * (1 - (max(self.min_value, min(self.max_value, self.current_value)) - self.min_value) / (self.max_value - self.min_value))\n",
        "\n",
        "        fig = go.Figure(\n",
        "            data=[\n",
        "                go.Pie(\n",
        "                    values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),\n",
        "                    rotation=90,\n",
        "                    hole=0.5,\n",
        "                    marker_colors=self.quadrant_colors,\n",
        "                    text=self.quadrant_text,\n",
        "                    textinfo=\"text\",\n",
        "                    hoverinfo=\"skip\",\n",
        "                ),\n",
        "            ],\n",
        "            layout=go.Layout(\n",
        "                showlegend=False,\n",
        "                margin=dict(b=0,t=10,l=10,r=10),\n",
        "                width=self.width,\n",
        "                height=self.height,\n",
        "                paper_bgcolor=self.quadrant_colors[0],\n",
        "                annotations=[\n",
        "                    go.layout.Annotation(\n",
        "                        text=f\"<b>{self.sensor_text}:</b><br>R$ :{self.current_value}\",\n",
        "                        x=0.5, xanchor=\"center\", xref=\"paper\",\n",
        "                        y=0.25, yanchor=\"bottom\", yref=\"paper\",\n",
        "                        showarrow=False,\n",
        "                    ),\n",
        "                ],\n",
        "                shapes=[\n",
        "                    go.layout.Shape(\n",
        "                        type=\"circle\",\n",
        "                        x0=0.48, x1=0.52,\n",
        "                        y0=0.48, y1=0.52,\n",
        "                        fillcolor=\"#333\",\n",
        "                        line_color=\"#333\",\n",
        "                    ),\n",
        "                    go.layout.Shape(\n",
        "                        type=\"line\",\n",
        "                        x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),\n",
        "                        y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),\n",
        "                        line=dict(color=\"#333\", width=4)\n",
        "                    )\n",
        "                ]\n",
        "            )\n",
        "        )\n",
        "        return fig\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Lucro_liquido = 2300\n",
        "# configs = [\n",
        "#     {\"current_value\": 2000, \"min_value\": 0, \"max_value\": 5000,\n",
        "#      \"quadrant_colors\": [\"#ffffff\", \"#f25829\", \"#f2a529\", \"#eff229\", \"#85e043\", \"#2bad4e\"],\n",
        "#      \"quadrant_text\": [\"\", \"<b style='font-size:10px;'>V high</b>\", \"<b style='font-size:10px;'>High</b>\", \"<b style='font-size:10px;'>M</b>\", \"<b style='font-size:10px;'>L</b>\", \"<b style='font-size:10px;'>Very l</b>\"],\n",
        "#      \"sensor_text\": \"Lucro Líquido\",},\n",
        "# ]\n",
        "\n",
        "# for config in configs:\n",
        "#     my_gauge = Pyplot(config[\"current_value\"], config[\"min_value\"], config[\"max_value\"], config[\"quadrant_colors\"], config[\"quadrant_text\"], config[\"sensor_text\"],width=600, height=400)\n",
        "#     fig = my_gauge.Bruno_gauge()\n",
        "#     fig.show()"
      ],
      "metadata": {
        "id": "4yupNnCZxEww"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ln-rWrYIvDLy"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
