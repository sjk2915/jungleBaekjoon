class Program
{
    static int N, M, V;
    static List<int>[] graph;
    static List<bool> visited;

    static void Main(string[] args)
    {
        int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        N = input[0]; M = input[1]; V = input[2];

        graph = new List<int>[N + 1];
        for (int i = 1; i < N + 1; i++)
        {
            graph[i] = new List<int>();
        }

        for (int i = 0; i < M; i++)
        {
            input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int u = input[0], v = input[1];

            graph[u].Add(v);
            graph[v].Add(u);
        }

        for (int i = 1; i < N + 1; i++)
        {
            graph[i].Sort();
        }

        List<int> answer = BFS(1);
        Console.WriteLine(string.Join(" ", answer));
    }

    static List<int> BFS(int start)
    {
        visited = new List<bool>(new bool[N + 1]);
        List<int> bfsPath = new List<int>();
        Queue<int> queue = new Queue<int>();

        visited[start] = true;
        bfsPath.Add(start);
        queue.Enqueue(start);
        while (queue.Count > 0)
        {
            int cur = queue.Dequeue();
            foreach (int next in graph[cur])
            {
                if (!visited[next])
                {
                    bfsPath.Add(next);
                    visited[next] = true;
                    queue.Enqueue(next);
                }
            }
        }
        return bfsPath;
    }
}