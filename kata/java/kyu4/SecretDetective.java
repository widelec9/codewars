package kyu4;

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class SecretDetective {
	/*
	def dfs(adj_list, v, visited, stack):
		visited[v] = True
		for k in adj_list[v]:
		    if not visited[k]:
		        dfs(adj_list, k, visited, stack)
		stack.insert(0, v)
	*/
	
	private void dfs(Map<Character, Set<Character>> adjMap, Character k, Map<Character, Boolean> visitedMap, Stack<Character> stack) {
		
	}
	
	public String recoverSecret(char[][] triplets) {
		Set<Character> charSet = Stream.of(triplets).map(String::new).flatMapToInt(String::chars).mapToObj(i->(char)i).collect(Collectors.toCollection(LinkedHashSet::new));
		Map<Character, Set<Character>> adjMap = new LinkedHashMap<>();
		for (Character ch : charSet) {
			adjMap.put(ch, new HashSet<Character>());
		}
		
		for (char[] t : triplets) {
			Set<Character> tempSet = new HashSet<Character>(); 
					
			tempSet = adjMap.get(t[0]);
			tempSet.add(t[1]);
			adjMap.replace(t[0], tempSet);
			
			tempSet = adjMap.get(t[1]);
			tempSet.add(t[2]);
			adjMap.replace(t[1], tempSet);
		}
		
		Map<Character, Boolean> visitedMap = new LinkedHashMap<>();
		for (Character k : adjMap.keySet()) {
			visitedMap.put(k, false);
		}
		
		Stack<Character> stack = new Stack<Character>();
		for (Character k : adjMap.keySet()) {
			if (!visitedMap.get(k)) {
				dfs(adjMap, k, visitedMap, stack);
			}
		}
		
		return "";
	}
}

/*
def dfs(adj_list, v, visited, stack):
	visited[v] = True
	for k in adj_list[v]:
	    if not visited[k]:
	        dfs(adj_list, k, visited, stack)
	stack.insert(0, v)


def recoverSecret(triplets):
	adj_list = {k: set() for k in set(sum(triplets, []))}
	for t in triplets:
	    adj_list[t[0]] |= {t[1]}
	    adj_list[t[1]] |= {t[2]}
	visited = {k: False for k in adj_list}
	stack = []
	for k in adj_list:
	    if not visited[k]:
	        dfs(adj_list, k, visited, stack)
	return ''.join(stack)
*/