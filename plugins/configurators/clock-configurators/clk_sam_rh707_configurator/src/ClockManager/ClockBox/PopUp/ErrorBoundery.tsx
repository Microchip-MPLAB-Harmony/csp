import React, { Component, ReactNode } from 'react';

interface ErrorBoundaryProps {
    fallback?: ReactNode; // The fallback UI to render in case of an error
    children: ReactNode;  // The children components wrapped by the boundary
}

interface ErrorBoundaryState {
    hasError: boolean;    // Tracks if an error has occurred
}

class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
    constructor(props: ErrorBoundaryProps) {
        super(props);
        this.state = { hasError: false };
    }

    static getDerivedStateFromError(): ErrorBoundaryState {
        // Update state to indicate an error occurred
        return { hasError: true };
    }

    componentDidCatch(error: Error, errorInfo: React.ErrorInfo): void {
        // Log the error details if needed
        console.error("ErrorBoundary caught an error:", error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            // Render fallback UI if an error occurred
            return this.props.fallback || <h1>Something went wrong.</h1>;
        }
        // Render children if no error
        return this.props.children;
    }
}

export default ErrorBoundary;
