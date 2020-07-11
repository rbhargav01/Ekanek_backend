import heapq
#delhi_to_mumbai: list of integers
#mumbai_to_delhi: list of integers
#k: integer
def k_cheap_flights(delhi_to_mumbai,mumbai_to_delhi,k):
    delhi_to_mumbai.sort()
    mumbai_to_delhi.sort()
    heap=[]
    heap.append([delhi_to_mumbai[0]+mumbai_to_delhi[0],0,0])
    ans=[]
    i1=0
    while(len(heap)>0 and i1<k):
        cur=heapq.heappop(heap)
        i=cur[1]
        j=cur[2]
        if(i<len(delhi_to_mumbai)-1):
            heapq.heappush(heap,[delhi_to_mumbai[i+1]+mumbai_to_delhi[j],i+1,j])
        if(j<len(mumbai_to_delhi)-1):
            heapq.heappush(heap,[delhi_to_mumbai[i]+mumbai_to_delhi[j+1],i,j+1])
        if(len(ans)>0 and [delhi_to_mumbai[i],mumbai_to_delhi[j]]==ans[-1]):
            continue
        ans.append([delhi_to_mumbai[i],mumbai_to_delhi[j]])
        i1+=1
    return ans

n=int(input("Enter the number of flights from Delhi to Mumbai: "))
delhi_to_mumbai=[]
for i in range(n):
    delhi_to_mumbai.append(int(input("Enter the fare for flight "+str(i+1)+": ")))
n=int(input("Enter the number of flights from Mumbai to Delhi: "))
mumbai_to_delhi=[]
for i in range(n):
    mumbai_to_delhi.append(int(input("Enter the fare for flight "+str(i+1)+": ")))
k=int(input("Enter the number of cheapest flights required: "))
print(k_cheap_flights(delhi_to_mumbai,mumbai_to_delhi,10))
