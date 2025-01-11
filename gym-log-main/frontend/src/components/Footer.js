const Footer = () => {
    return (
        <footer className="text-center bg-light pt-1">
            <span>Made with <i className="fa fa-heart"/> by </span>
            <a href={process.env.REACT_APP_AUTHOR_LINKEDIN_URL} target="_blank" rel="noreferrer">
                Hlonela Clyde Madubela
            </a>

            <div>
                <span> ©2025</span>
            </div>
        </footer>
    );
};

export default Footer;
