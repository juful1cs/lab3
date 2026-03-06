{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6b1ef389-fd3d-4085-95b9-71a00203bc55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter password:  admin123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Access Granted\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adult\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive\n",
      "Number is between 10 and 50\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a color (red, yellow, green):  green\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Go\n",
      "Menu\n",
      "1. Addition\n",
      "2. Subtraction\n",
      "3. Multiplication\n",
      "4. Division\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose option:  1\n",
      "Enter first number:  10\n",
      "Enter second number:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 15.0\n"
     ]
    }
   ],
   "source": [
    "# Question 1\n",
    "password = input(\"Enter password: \")\n",
    "\n",
    "if password == \"admin123\":\n",
    "    print(\"Access Granted\")\n",
    "else:\n",
    "    print(\"Access Denied\")\n",
    "\n",
    "\n",
    "# Question 2\n",
    "age = int(input(\"Enter your age: \"))\n",
    "\n",
    "if age < 13:\n",
    "    print(\"Child\")\n",
    "elif age >= 13 and age <= 19:\n",
    "    print(\"Teen\")\n",
    "elif age >= 20 and age <= 59:\n",
    "    print(\"Adult\")\n",
    "else:\n",
    "    print(\"Senior\")\n",
    "\n",
    "\n",
    "# Question 3\n",
    "num = int(input(\"Enter a number: \"))\n",
    "\n",
    "if num > 0:\n",
    "    print(\"Positive\")\n",
    "else:\n",
    "    print(\"Not Positive\")\n",
    "\n",
    "if num >= 10 and num <= 50:\n",
    "    print(\"Number is between 10 and 50\")\n",
    "else:\n",
    "    print(\"Number is not between 10 and 50\")\n",
    "\n",
    "\n",
    "# Question 4\n",
    "color = input(\"Enter a color (red, yellow, green): \")\n",
    "\n",
    "if color != \"\":\n",
    "    match color:\n",
    "        case \"red\":\n",
    "            print(\"Stop\")\n",
    "        case \"yellow\":\n",
    "            print(\"Ready\")\n",
    "        case \"green\":\n",
    "            print(\"Go\")\n",
    "        case _:\n",
    "            print(\"Wrong color\")\n",
    "else:\n",
    "    print(\"Input is empty\")\n",
    "\n",
    "\n",
    "# Question 5\n",
    "print(\"Menu\")\n",
    "print(\"1. Addition\")\n",
    "print(\"2. Subtraction\")\n",
    "print(\"3. Multiplication\")\n",
    "print(\"4. Division\")\n",
    "\n",
    "choice = input(\"Choose option: \")\n",
    "\n",
    "n1 = float(input(\"Enter first number: \"))\n",
    "n2 = float(input(\"Enter second number: \"))\n",
    "\n",
    "match choice:\n",
    "    case \"1\":\n",
    "        print(\"Result:\", n1 + n2)\n",
    "    case \"2\":\n",
    "        print(\"Result:\", n1 - n2)\n",
    "    case \"3\":\n",
    "        print(\"Result:\", n1 * n2)\n",
    "    case \"4\":\n",
    "        print(\"Result:\", n1 / n2)\n",
    "    case _:\n",
    "        print(\"Invalid option\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9f17430-3596-4748-ad0e-d3db0f25b843",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
