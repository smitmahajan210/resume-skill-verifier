import Link from "next/link";

export default function Home() {
  return (
    <main>
      <h1>AI Resume Skill Verifier</h1>
      <p>
        Open the upload page to submit a resume:{" "}
        <Link href="/upload">/upload</Link>
      </p>
    </main>
  );
}
