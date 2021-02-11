{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "test.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP7dl3G0kGZT8MBB+KV2f63",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/husaun510/DS_Project2_World_Cloud/blob/https%2Fgithub.com%2Fheroku%2Fpython-getting-started/test_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PtLsKWRyMwta",
        "outputId": "e46ee6e5-7807-4594-d542-d75b342d130b"
      },
      "source": [
        "!git clone https://github.com/husaun510/DS_Project2_World_Cloud"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cloning into 'DS_Project2_World_Cloud'...\n",
            "remote: Enumerating objects: 205, done.\u001b[K\n",
            "remote: Total 205 (delta 0), reused 0 (delta 0), pack-reused 205\u001b[K\n",
            "Receiving objects: 100% (205/205), 46.90 KiB | 2.23 MiB/s, done.\n",
            "Resolving deltas: 100% (82/82), done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uJCv0bT_NFlm",
        "outputId": "6dc17c38-b1f0-4c83-fa7d-818fa395d34a"
      },
      "source": [
        "!cat /content/DS_Project2_World_Cloud/app.py"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "import cv2\n",
            "import tweepy\n",
            "from wordcloud import WordCloud\n",
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "from flask import Flask, render_template, request\n",
            "# from flask_ngrok import run_with_ngrok\n",
            "#husain\n",
            "\n",
            "consumer_key='fbR5kFHpU8qExKleXnefRzQfQ'\n",
            "consumer_secret='T1c53pX0WDEgX7IEIwD4MhMwFBZ1HTZj5ZJKZ4WrzhDSehK2kg'\n",
            "access_token_key='510740882-eI8mtDqxIlJlrl5QAkKRJWKsxfXTd3KhAHTFyUUI'\n",
            "access_token_secret='4HGd0XyuEXMg8m0k2HoP4yjnqpCDZlvSOLi5NvLGme47g'\n",
            "\n",
            "auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)\n",
            "\n",
            "auth.set_access_token(access_token_key, access_token_secret)\n",
            "\n",
            "api = tweepy.API(auth)\n",
            "\n",
            "\n",
            "app = Flask(__name__)\n",
            "# run_with_ngrok(app)\n",
            "@app.route('/')\n",
            "\n",
            "def Hashtag():\n",
            "   return render_template('Hashtag.html')\n",
            "\n",
            "@app.route('/result',methods = ['POST', 'GET'])\n",
            "def result():\n",
            "   if request.method == 'POST':\n",
            "      result = request.form['hash']\n",
            "      tweets = tweepy.Cursor(api.search, q=result, lang=\"en\").items(100)\n",
            "      cloud = \"\"\n",
            "      for each in tweets:\n",
            "          cloud = cloud + each.text\n",
            "\n",
            "      cloud = WordCloud(background_color=\"white\").generate(cloud)\n",
            "\n",
            "      # plt.imshow(cloud)\n",
            "\n",
            "      image = np.array(cloud)\n",
            "      cv2.imwrite('static/cloud.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 100])\n",
            "\n",
            "      return render_template(\"result.html\",result = result)\n",
            "\n",
            "if __name__ == '__main__':\n",
            "   app.run()\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4kw_9vblQHvl",
        "outputId": "a44932b9-662b-4045-a284-42078b7f9408"
      },
      "source": [
        "import cv2\r\n",
        "import tweepy\r\n",
        "from wordcloud import WordCloud\r\n",
        "import matplotlib.pyplot as plt\r\n",
        "import numpy as np\r\n",
        "from flask import Flask, render_template, request\r\n",
        "# from flask_ngrok import run_with_ngrok\r\n",
        "#husain\r\n",
        "\r\n",
        "consumer_key='fbR5kFHpU8qExKleXnefRzQfQ'\r\n",
        "consumer_secret='T1c53pX0WDEgX7IEIwD4MhMwFBZ1HTZj5ZJKZ4WrzhDSehK2kg'\r\n",
        "access_token_key='510740882-eI8mtDqxIlJlrl5QAkKRJWKsxfXTd3KhAHTFyUUI'\r\n",
        "access_token_secret='4HGd0XyuEXMg8m0k2HoP4yjnqpCDZlvSOLi5NvLGme47g'\r\n",
        "\r\n",
        "auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)\r\n",
        "\r\n",
        "auth.set_access_token(access_token_key, access_token_secret)\r\n",
        "\r\n",
        "api = tweepy.API(auth)\r\n",
        "\r\n",
        "\r\n",
        "app = Flask(__name__)\r\n",
        "# run_with_ngrok(app)\r\n",
        "@app.route('/')\r\n",
        "\r\n",
        "def Hashtag():\r\n",
        "   return render_template('Hashtag.html')\r\n",
        "\r\n",
        "@app.route('/result',methods = ['POST', 'GET'])\r\n",
        "def result():\r\n",
        "   if request.method == 'POST':\r\n",
        "      result = request.form['hash']\r\n",
        "      tweets = tweepy.Cursor(api.search, q=result, lang=\"en\").items(100)\r\n",
        "      cloud = \"\"\r\n",
        "      for each in tweets:\r\n",
        "          cloud = cloud + each.text\r\n",
        "\r\n",
        "      cloud = WordCloud(background_color=\"white\").generate(cloud)\r\n",
        "\r\n",
        "      # plt.imshow(cloud)\r\n",
        "\r\n",
        "      image = np.array(cloud)\r\n",
        "      cv2.imwrite('static/cloud.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 100])\r\n",
        "\r\n",
        "      return render_template(\"result.html\",result = result)\r\n",
        "\r\n",
        "if __name__ == '__main__':\r\n",
        "   app.run()"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " * Serving Flask app \"__main__\" (lazy loading)\n",
            " * Environment: production\n",
            "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
            "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
            " * Debug mode: off\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FRCHpmuzQMG3"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}