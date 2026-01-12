{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "609e89c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Shapes import circle, rectangle\n",
    "\n",
    "# Circle\n",
    "r = float(input(\"Enter radius of the circle: \"))\n",
    "print(\"Circle Area:\", circle.area(r))\n",
    "print(\"Circle Perimeter:\", circle.perimeter(r))\n",
    "\n",
    "# Rectangle\n",
    "l = float(input(\"Enter length of the rectangle: \"))\n",
    "b = float(input(\"Enter breadth of the rectangle: \"))\n",
    "\n",
    "print(\"Rectangle Area:\", rectangle.area(l, b))\n",
    "print(\"Rectangle Perimeter:\", rectangle.perimeter(l, b))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
