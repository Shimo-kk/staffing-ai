'use client';
import Image from "next/image";
import { Button } from "@heroui/button";

/**
 * エラーページ
 * @returns {JSX.Element} エラーページのHTML構造
 */
export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <div className="w-screen h-screen bg-white">
      <div className="text-center">
        <div className="flex justify-center py-12">
          <Image
            src="/logo.svg"
            alt="Logo"
            width={270}
            height={180}
          />
        </div>
        <div className="p-8 text-center">
          <h1 className="text-4xl text-black font-bold mb-4">問題が発生しました</h1>
          <p className="text-subfont mb-6">{error.message}</p>
          <Button
            color="primary"
            onPress={() => reset()}
          >
            再試行
          </Button>
        </div>
      </div>
    </div>
  );
}
