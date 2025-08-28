'use client'

import { Breadcrumbs, BreadcrumbItem } from "@heroui/breadcrumbs";

export interface BreadcrumbItemType {
  label: string;
  href?: string;
}

interface Props {
  items: BreadcrumbItemType[];
  className?: string;
}

/**
 * パンくずコンポーネント
 * @param items - パンくずの項目配列
 * @param className - 追加のCSSクラス
 * @returns {JSX.Element} パンくずのHTML構造
 */
export default function Breadcrumb({ items, className = "" }: Props) {
  return (
    <div className={`w-full p-2 ${className}`}>
      <Breadcrumbs>
        {items.map((item, index) => (
          <BreadcrumbItem
            key={index}
            href={item.href}
          >
            {item.label}
          </BreadcrumbItem>
        ))}
      </Breadcrumbs>
    </div>
  );
} 