$port = 8000
$listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, $port)
$listener.Start()

Write-Host "Signe de vie server listening on http://localhost:8000/"
Write-Host "Press Ctrl+C to stop."

try {
    while ($true) {
        $client = $listener.AcceptTcpClient()

        try {
            $stream = $client.GetStream()
            $buffer = New-Object byte[] 4096
            $read = $stream.Read($buffer, 0, $buffer.Length)
            $request = [System.Text.Encoding]::ASCII.GetString($buffer, 0, $read)
            $firstLine = ($request -split "`r?`n")[0]

            if ($firstLine -match "^GET /health ") {
                $body = "OK - mission 1 alive`n"
            } else {
                $body = "Signe de vie`n"
            }

            $bodyBytes = [System.Text.Encoding]::UTF8.GetBytes($body)
            $headers = "HTTP/1.1 200 OK`r`nContent-Type: text/plain; charset=utf-8`r`nContent-Length: $($bodyBytes.Length)`r`nConnection: close`r`n`r`n"
            $headerBytes = [System.Text.Encoding]::ASCII.GetBytes($headers)

            $stream.Write($headerBytes, 0, $headerBytes.Length)
            $stream.Write($bodyBytes, 0, $bodyBytes.Length)
        }
        finally {
            $client.Close()
        }
    }
}
finally {
    $listener.Stop()
    $listener.Close()
}
