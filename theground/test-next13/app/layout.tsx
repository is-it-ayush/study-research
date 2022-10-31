export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <head>
        <title>Next.js Playground</title>
      </head>
      <body>{children}</body>
    </html>
  );
}
