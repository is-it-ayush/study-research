export default async function Home({ name }: { name: string }) {
  const res = await fetch("http://localhost:3000/api/hello");
  const data = await res.json();

  console.log(`data`, data);

  return (
    <div className="">
      <main className="">
        <h1 className="">Hi, This is route `/`. Your name is {name}</h1>
      </main>
    </div>
  );
}
