Production-Server-for-Encrypted-FT-Token-GEN

To get started go to the Agora website and make an account -> now create a project and retreive the app ID and certificate

-> replace them in the server file

Go to Heroku website and make an account and downdload the CLI

Then make an app

In VS code add in the files, log in with the command propmt using heroku login

Then use git add to add the files

commit the files

finally push the app to heroku. Pass a channel ID and user UID by requesting the url:
https://appname-3e34a4a2709c.herokuapp.com/process_data?x=UID&y=channelname

From a swift project to fetch a user token run:
```
let x = 21
let y = "hello"
let serverIP = "http://[2601:1c0:8484:32a0:b95a:bf8f:a65a:f73e]:5000"

func sendDataToServer(x: Int, y: String, completion: @escaping (String?) -> Void) {
    // Specify both parameters in the URL
    if let url = URL(string: "\(serverIP)/process_data?x=\(x)&y=\(y)") {
        URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let data = data {
                do {
                    if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any],
                       let result = json["result"] as? String {
                        completion(result)
                    }
                } catch {
                    print(error.localizedDescription)
                    completion(nil)
                }
            }
        }.resume()
    }
}

// Example usage with specified x and y parameters
sendDataToServer(x: x, y: y) { (result) in
    if let result = result {
        print("Server response: \(result)")
    } else {
        print("Failed to process data on the server")
    }
}

```
