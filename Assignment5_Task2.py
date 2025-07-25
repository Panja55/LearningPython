x=[i for i in range(1,11)]
print("Original list:",x)
a=x[:5]
print("Extracted first five elements:",a)
#Method-1
print("Reversed extracted elements:",a[::-1])
#Method-2
r_it=reversed(a)
print("Reversed extracted elements:",list(r_it))
#Method-3
a.reverse()
print("Reversed extracted elements:",a)