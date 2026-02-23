import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import { Providers } from "@/components/Providers";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AddManuChain — On-Demand Certified Parts for Remote Operations",
  description: "When a part fails at sea, every hour costs $50,000–$100,000. AddManuChain connects OEM blueprint owners, certified 3D-printing centers, and offshore operators — delivering LR/DNV-certified parts in days, not weeks.",
  keywords: ["AddManuChain", "additive manufacturing", "3D printing", "offshore", "naval", "certified parts", "supply chain", "maritime", "remote operations", "DNV", "Lloyd's Register"],
  authors: [{ name: "AddManuChain Team" }],
  icons: {
    icon: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230EA5E9' stroke-width='2'><path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/></svg>",
  },
  openGraph: {
    title: "AddManuChain — On-Demand Certified Parts",
    description: "Delivering LR/DNV-certified parts in days, not weeks for offshore and remote operations.",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "AddManuChain",
    description: "On-demand certified parts for remote operations",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${inter.variable} font-sans antialiased bg-background text-foreground`}
      >
        <Providers>
          {children}
          <Toaster />
        </Providers>
      </body>
    </html>
  );
}
