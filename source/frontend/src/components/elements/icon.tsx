"use client";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

type Props = {
  icon: IconDefinition;
  className?: string;
};

/**
 * アイコンコンポーネント
 * @returns {JSX.Element} HTML構造
 */
export default function Icon({ icon, className }: Props) {
  return <FontAwesomeIcon icon={icon} className={className} />;
};
