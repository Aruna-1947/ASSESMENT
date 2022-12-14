{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
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
      "cell_type": "code",
      "execution_count": 46,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "50LsvpjNCzPY",
        "outputId": "a576892e-f2ed-45d8-b420-af26442b24c7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "uploaded\n",
            "DIFFERENT FILES\n",
            "sample1.json  FILE TYPE :  json\n",
            "sample2.pdf  FILE TYPE :  pdf\n"
          ]
        }
      ],
      "source": [
        "# UPLOAD FILES\n",
        "import requests\n",
        "test_files={\"test1\": open(\"sample2.pdf\",\"rb\"),\"test2\":open(\"sample1.json\",\"rb\")}\n",
        "# test_files={\"test1\": open(\"sample2.pdf\",\"rb\"),\"test2\":open(\"sample1.json\",\"rb\"),\"test3\":open(\"sample1.json\",\"rb\")}\n",
        "n=len(test_files)\n",
        "if n==2:\n",
        "  test_url=\"http://httpbin.org/post\"\n",
        "  test_response = requests.post(test_url,files=test_files)\n",
        "  if test_response.ok:\n",
        "    print(\"uploaded\")\n",
        "  else:\n",
        "    print(\"error\")\n",
        "else:\n",
        "  print(\"MORE THAN 2 FILE\")\n",
        "\n",
        "# FIND FILE SAME OR NOT\n",
        "\n",
        "import hashlib\n",
        "from difflib import SequenceMatcher\n",
        "def hash_file(fileName1,fileName2):\n",
        "  h1=hashlib.sha1()\n",
        "  h2=hashlib.sha1()\n",
        "  with open(fileName1,\"rb\") as file:\n",
        "    chunk=0\n",
        "    while chunk!=b'':\n",
        "      chunk=file.read(1024)\n",
        "      h1.update(chunk)\n",
        "  with open(fileName2,\"rb\") as file:\n",
        "    chunk=0\n",
        "    while chunk!=b'':\n",
        "      chunk=file.read(1024)\n",
        "      h2.update(chunk)\n",
        "  return h1.hexdigest(),h2.hexdigest()\n",
        "msg1,msg2=hash_file(\"sample1.json\",\"sample2.pdf\")\n",
        "if msg1==msg2:\n",
        "  print('SAME FILES')\n",
        "else:\n",
        "  print('DIFFERENT FILES')\n",
        "# print(msg1+\"\\t\"+msg2)\n",
        "\n",
        "\n",
        "import re\n",
        "\n",
        "def checkext(fname):   \n",
        "    if re.search('\\.json$',fname,flags=re.IGNORECASE):\n",
        "        return('json')\n",
        "    if re.search('\\.pdf$',fname,flags=re.IGNORECASE):\n",
        "        return('pdf')\n",
        "    return('skip')\n",
        "\n",
        "flist = ['sample1.json', 'sample2.pdf']\n",
        "\n",
        "for f in flist:\n",
        "  print(f,\" FILE TYPE : \",checkext(f)) \n"
      ]
    }
  ]
}
