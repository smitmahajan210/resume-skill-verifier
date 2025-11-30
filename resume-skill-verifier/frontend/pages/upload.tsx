import { useState } from "react";
import axios from "axios";

export default function Upload() {
    const [file, setFile] = useState<File | null>(null);

    const handleUpload = async () => {
        if (!file) return;
        const formData = new FormData();
        formData.append("resume", file);
        await axios.post("http://localhost:8000/resumes/upload", formData);
        alert("Uploaded!");
    }

    return (
        <div>
            <input type="file" onChange={e => setFile(e.target.files?.[0] || null)} />
            <button onClick={handleUpload}>Upload Resume</button>
        </div>
    )
}