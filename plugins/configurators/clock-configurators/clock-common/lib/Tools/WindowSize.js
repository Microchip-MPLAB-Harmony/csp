"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
function getWindowDimensions() {
    const { innerWidth: width, innerHeight: height } = window;
    return {
        width,
        height
    };
}
function useWindowDimensions() {
    const [windowDimensions, setWindowDimensions] = (0, react_1.useState)(getWindowDimensions());
    (0, react_1.useEffect)(() => {
        function handleResize() {
            setWindowDimensions(getWindowDimensions());
        }
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);
    return windowDimensions;
}
exports.default = useWindowDimensions;
