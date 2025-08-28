import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { ToastProvider } from "@heroui/toast";

/**
 * Geist Sans フォントの設定
 */
const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

/**
 * Geist Mono フォントの設定
 */
const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

/**
 * アプリケーションのメタデータ設定
 */
export const metadata: Metadata = {
  title: "Staffing AI",
  description: "Staffing AI",
};

/**
 * ルートレイアウトコンポーネント
 * @param {Object} props - プロパティオブジェクト
 * @param {React.ReactNode} props.children - 子コンポーネント
 * @returns ルートレイアウトのReactノード
 */
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <ToastProvider placement="bottom-center" />
        {children}
      </body>
    </html>
  );
}
