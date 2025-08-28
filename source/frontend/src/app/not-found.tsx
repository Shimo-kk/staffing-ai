'use client'

import { useRouter } from "next/navigation";
import Image from "next/image";
import { Button } from "@heroui/button";

/**
 * 404エラーページ
 * @returns {JSX.Element} 404エラーページのHTML構造
 */
export default function NotFound() {
  const router = useRouter();

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
          <h1 className="text-4xl text-black font-bold mb-4">ページが見つかりません</h1>
          <p className="text-subfont mb-6">お探しのページは存在しないか、移動した可能性があります。</p>
          <Button
            type="button"
            color="primary"
            onPress={() => {
              router.back();
            }}
          >
            戻る
          </Button>
        </div>
      </div>
    </div>
  );
}
