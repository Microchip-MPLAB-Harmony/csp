"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = __importDefault(require("react"));
const button_1 = require("primereact/button");
const toolbar_1 = require("primereact/toolbar");
const microchip_icon_png_1 = __importDefault(require("../resources/images/microchip_icon.png"));
require("./toolbar.css");
const api_1 = __importDefault(require("primereact/api"));
const NodeUtils_1 = require("@mplab_harmony/harmony-plugin-ui/build/utils/NodeUtils");
const ProjectService_1 = require("@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService");
const clock_common_1 = require("clock-common");
const Toolbar = (props) => {
    api_1.default.ripple = true;
    const leftContents = (react_1.default.createElement(react_1.default.Fragment, null,
        (0, NodeUtils_1.LoadImage)(microchip_icon_png_1.default),
        react_1.default.createElement("label", { style: { fontSize: '18px', fontWeight: 'bolder' } },
            " ",
            props.title,
            " ")));
    const rightContents = (react_1.default.createElement(react_1.default.Fragment, null,
        react_1.default.createElement(button_1.Button, { label: 'HOME', tooltip: `View ${props.title} Home Screen`, tooltipOptions: { position: 'bottom' }, icon: 'pi pi-home', iconPos: 'left', className: 'p-button p-button-text mr-2', style: { fontWeight: 'bold', color: 'black' }, onClick: () => LoadHome() }),
        react_1.default.createElement(button_1.Button, { label: 'SUMMARY', tooltip: 'View Summary', tooltipOptions: { position: 'bottom' }, className: 'p-button p-button-text  mr-2', style: { fontWeight: 'bold', color: 'black' }, onClick: () => LoadSummary() }),
        react_1.default.createElement(button_1.Button, { label: 'HELP', tooltip: 'View Clock Configuration help', tooltipOptions: { position: 'bottom' }, className: 'p-button p-button-text  mr-2', iconPos: 'right', style: { fontWeight: 'bold', color: 'black' }, onClick: () => clock_common_1.pluginService.openURL(props.helpUrl) }),
        react_1.default.createElement(button_1.Button, { tooltip: 'Ctrl + Mouse Scroll Up', tooltipOptions: { position: 'left' }, icon: 'pi pi-search-plus', className: 'p-button-rounded p-button-text p-button-plain p-button-lg mr-1', onClick: () => ZoomIn() }),
        react_1.default.createElement(button_1.Button, { tooltip: 'Ctrl + Mouse Scroll Down', tooltipOptions: { position: 'left' }, icon: 'pi pi-search-minus', className: 'p-button-rounded p-button-text p-button-lg p-button-plain', onClick: () => ZoomOut() })));
    const HideAll = () => {
        (0, NodeUtils_1.HideDiv)(document.getElementById('home'));
        (0, NodeUtils_1.HideDiv)(document.getElementById('summary'));
    };
    const LoadHome = () => {
        HideAll();
        (0, NodeUtils_1.ShowDiv)(document.getElementById('home'), null);
    };
    const LoadSummary = () => {
        HideAll();
        (0, NodeUtils_1.ShowDiv)(document.getElementById('summary'), null);
    };
    function ZoomIn() {
        (0, ProjectService_1.ZoomInReact)();
    }
    function ZoomOut() {
        (0, ProjectService_1.ZoomOutReact)();
    }
    return (react_1.default.createElement("div", { className: 'Headder' },
        react_1.default.createElement("div", null,
            react_1.default.createElement(toolbar_1.Toolbar, { left: leftContents, right: rightContents, style: { background: 'white', height: 60, border: 'white' } }))));
};
exports.default = Toolbar;
