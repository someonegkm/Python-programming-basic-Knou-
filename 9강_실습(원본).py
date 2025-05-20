{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/someonegkm/1st_Project/blob/main/9%EA%B0%95_%EC%8B%A4%EC%8A%B5(%EC%9B%90%EB%B3%B8).ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 9강 1절"
      ],
      "metadata": {
        "id": "CAj_VKRq4Mhy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**원뿔 부피 계산 함수 정의**"
      ],
      "metadata": {
        "id": "-0FrgkDm_YRK"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "OhGWjvMSf_uP"
      },
      "outputs": [],
      "source": [
        "def prt_cone_vol(r, h) :\n",
        "    if r > 0 and h > 0 :\n",
        "        # r, h 모두 양수일 때\n",
        "        vol = 1/3 * 3.14 * r ** 2 * h\n",
        "        print(\"원뿔의 부피는\", vol, \"입니다.\")\n",
        "    else :\n",
        "        # r, h가 음수일 때\n",
        "        print(\"반지름과 높이 값에 양수를 입력하세요\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**원뿔 부피 계산 함수 호출**"
      ],
      "metadata": {
        "id": "ygj-h_dt_elG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "radius = int(input(\"반지름을 입력하세요: \"))\n",
        "height = int(input(\"높이를 입력하세요: \"))\n",
        "\n",
        "prt_cone_vol(radius, height)"
      ],
      "metadata": {
        "id": "Kgl7g457gFnj",
        "outputId": "99ca9238-75b7-4a29-9829-41e5b431bf55",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "반지름을 입력하세요: 30\n",
            "높이를 입력하세요: 20\n",
            "원뿔의 부피는 18840.0 입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**숫자를 입력받고 역순으로 출력하는 함수를 사용한 프로그램 문제**"
      ],
      "metadata": {
        "id": "3T0GpqYK_jXA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num = 1234\n",
        "#매개변수 num은 정의된 함수 내에서만 사용\n",
        "def reverse_number(num) :\n",
        "    while num > 0 :\n",
        "        digit = num % 10 # %는 나머지 연산자 나눈 뒤 나머지 값만 출력\n",
        "        num = num // 10 #num에 덮어쓰기 됨, 정수 나눗셈/나눈 뒤 소수점은 버림\n",
        "        print(digit, end=\"\")\n",
        "\n",
        "reverse_number(num)\n"
      ],
      "metadata": {
        "id": "nsHHCmKB_pnQ",
        "outputId": "7a9afcd5-9bff-481e-e93d-580ae842ebba",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4321"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 9강 2절"
      ],
      "metadata": {
        "id": "bw1IBTsp4wMv"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**원뿔 부피 계산 결과 반환 함수 정의**"
      ],
      "metadata": {
        "id": "454aKvSdAI2a"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def rtn_cone_vol(r, h) :\n",
        "    if r > 0 and h > 0 :\n",
        "        #r,h 모두 양수 일 때\n",
        "        vol = 1/3 * 3.14 * r ** 2 * h\n",
        "        print(\"원뿔의 부피는\", vol, \"입니다.\")\n",
        "        return vol\n",
        "    else :\n",
        "        #r, h가 모두 음수일 때\n",
        "        print(\"반지름과 높이 값에 양수를 입력하세요.\")\n",
        "\n",
        "print(format(rtn_cone_vol(10, 20),\"<20.3f\"), \"입니다.\")"
      ],
      "metadata": {
        "id": "X8lfqqRBAQfV",
        "outputId": "53a37a31-4441-4bbc-d748-f964d2ef4614",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "원뿔의 부피는 2093.333333333333 입니다.\n",
            "2093.333             입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**원뿔 부피 및 겉넓이 반환 함수 정의**"
      ],
      "metadata": {
        "id": "Ae2D5Cal_szh"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cwZ6g1au45RD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**세 개의 사용자 입력을 오름차순으로 정렬하는 함수를 이용하여 정렬된 값을 출력하는 문제**\n"
      ],
      "metadata": {
        "id": "0FMNpd_4Ah9j"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input(\"첫번째 숫자를 입력하세요: \"))\n",
        "b = int(input(\"첫번째 숫자를 입력하세요: \"))\n",
        "c = int(input(\"첫번째 숫자를 입력하세요: \"))\n",
        "\n",
        "def sort3(a, b, c) :"
      ],
      "metadata": {
        "id": "toh-zjeLArWn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 9강 3절"
      ],
      "metadata": {
        "id": "7qOMFABd4y1t"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**값의 전달**"
      ],
      "metadata": {
        "id": "pVwxXsFLBCY-"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cwoR_CQp45ti"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**변수의 스코프**"
      ],
      "metadata": {
        "id": "Wybq2K3yBJ8C"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6ZuNFN9BBWKR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**단위 원뿔(반지름 20, 높이 30)의 부피와 겉넓이를 출력하는 문제**"
      ],
      "metadata": {
        "id": "YDpFj9zqBL35"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 원뿔 계산 함수 정의\n",
        "def prt_cone_vol_surf(r, h) :\n",
        "    if r > 0 and h > 0 :\n",
        "        # r, h 모두 양수일 때\n",
        "        vol = 1/3 * 3.14 * r ** 2 * h\n",
        "        suf = 3.14 * r ** 2 + 3.14 * r * h\n",
        "        return vol, surf\n",
        "    else :\n",
        "        # r, h가 음수일 때\n",
        "        print(\"반지름과 높이 값에 양수를 입력하세요\")\n"
      ],
      "metadata": {
        "id": "mzWTObQdBXHc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**여러개의 수를 입력받고 합과 평균을 반환하는는 var_sum_avg 함수를 사용하여, (20, 25, 10, 85, 100, 150)에 대한 합과 평균을 출력하는 프로그램을 작성하시오.**\n"
      ],
      "metadata": {
        "id": "WqqJAJ0ACOjj"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "GDZkR-SKCVth"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
