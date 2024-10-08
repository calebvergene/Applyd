import React, { useState, useRef, useEffect } from 'react';

interface DropdownItem {
  label: string;
  onClick: () => void;
}

interface CustomDropdownProps {
  label: React.ReactNode;
  items: DropdownItem[];
}

const CustomDropdown: React.FC<CustomDropdownProps> = ({ label, items }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<{ icon: React.ReactNode, label: string } | null>(null); 
  const dropdownRef = useRef<HTMLDivElement>(null);

  const toggleDropdown = () => setIsOpen(!isOpen);

  const handleClickOutside = (event: MouseEvent) => {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const handleDropdownClick = (icon: React.ReactNode, item: DropdownItem) => {
    item.onClick();
    setSelectedItem({ icon, label: item.label });
    setIsOpen(false);
  };

  const getStatusClassName = (status: string) => {
    switch (status) {
      case "Not Applied":
        return "text-neutral-400 mr-2";
      case "Applied":
        return "text-blue-500 mr-2";
      case "Interviewing":
        return "text-yellow-300 mr-2";
      case "Offered":
        return "text-green-400 mr-2";
      case "Rejected":
        return "text-red-500 mr-2";
      default:
        return "";
    }
  };

  return (
    <div className="relative inline-block text-left font-rubik" ref={dropdownRef}>
      <div
        className={`flex items-center justify-center my-1 z-${isOpen ? '20' : '20'}`}
        style={{ zIndex: isOpen ? 20 : 20 }}
      >
        <button
          onClick={toggleDropdown}
          className="bg-transparent p-2 py-2 text-md flex items-center justify-center rounded-lg hover:p-1 hover:px-2 hover:mt-1 hover:bg-gray-300/50 hover:mb-1 duration-300"
        >
          {selectedItem ? (
            <>
              {selectedItem.icon} {selectedItem.label}
            </>
          ) : (
            label
          )}
          {label === "Sort By" && (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="1em"
              height="1em"
              viewBox="0 0 24 24"
              className="ml-2"
            >
              <path
                fill="currentColor"
                d="M16.29 14.29L12 18.59l-4.29-4.3a1 1 0 0 0-1.42 1.42l5 5a1 1 0 0 0 1.42 0l5-5a1 1 0 0 0-1.42-1.42M7.71 9.71L12 5.41l4.29 4.3a1 1 0 0 0 1.42 0a1 1 0 0 0 0-1.42l-5-5a1 1 0 0 0-1.42 0l-5 5a1 1 0 0 0 1.42 1.42"
              />
            </svg>
          )}
        </button>
      </div>
      {isOpen && (
        <div className="absolute left-1/2 transform -translate-x-1/2 w-28 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-50">
          <div className="z-50" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
            {items.map((item, index) => (
              <button
                key={index}
                onClick={() => handleDropdownClick(
                  item.label !== "Similarity" ? <span className={getStatusClassName(item.label)}> ● </span> : null,
                  item
                )}                className={`block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:rounded-sm w-full text-center z-50 ${
                  item.label === 'Similarity' ? 'border-t border-gray-300' : ''
                }`}
                role="menuitem"
              >
                {item.label}
              </button>
            ))}
          </div>
        </div>
      )}

    </div>
  );
};

export default CustomDropdown;
