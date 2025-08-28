'use client'

import { ReactNode } from "react";

interface Props {
  children?: ReactNode;
  className?: string;
}

/**
 * コンテンツエリアコンポーネント
 * @param children - 子要素
 * @param className - 追加のCSSクラス
 * @returns {JSX.Element} コンテンツエリアのHTML構造
 */
export default function ContentsArea({ children, className = "" }: Props) {
  return (
    <div className={`max-w-screen-xl mx-auto px-2 pt-2 pb-8 ${className}`}>
      {children}
    </div>
  );
} 