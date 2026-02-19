import type { Metadata } from "next";
import Script from "next/script";
import "./globals.css";

export const metadata: Metadata = {
  title: "Gofly - Tour & Travel Booking Website.",
  description: "Tour & Travel Booking Website.",
  icons: {
    icon: "/images/fav-icon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link href="/css/bootstrap.min.css" rel="stylesheet" />
        <link href="/css/jquery-ui.css" rel="stylesheet" />
        <link href="/css/bootstrap-icons.css" rel="stylesheet" />
        <link href="/css/animate.min.css" rel="stylesheet" />
        <link href="/css/jquery.fancybox.min.css" rel="stylesheet" />
        <link rel="stylesheet" href="/css/swiper-bundle.min.css" />
        <link rel="stylesheet" href="/css/slick.css" />
        <link rel="stylesheet" href="/css/slick-theme.css" />
        <link rel="stylesheet" href="/css/daterangepicker.css" />
        <link href="/css/boxicons.min.css" rel="stylesheet" />
        <link rel="stylesheet" href="/css/style.css" />
      </head>
      <body className="tt-magic-cursor">
        <div id="magic-cursor">
          <div id="ball"></div>
        </div>

        {children}

        {/* Scripts */}
        <Script src="/js/jquery-3.7.1.min.js" strategy="beforeInteractive" />
        <Script src="/js/jquery-ui.js" strategy="beforeInteractive" />
        <Script src="/js/moment.min.js" strategy="beforeInteractive" />
        <Script src="/js/daterangepicker.min.js" strategy="beforeInteractive" />
        <Script src="/js/bootstrap.min.js" strategy="beforeInteractive" />
        <Script src="/js/popper.min.js" strategy="beforeInteractive" />
        <Script src="/js/swiper-bundle.min.js" strategy="beforeInteractive" />
        <Script src="/js/slick.js" strategy="beforeInteractive" />
        <Script src="/js/waypoints.min.js" strategy="beforeInteractive" />
        <Script src="/js/jquery.counterup.min.js" strategy="beforeInteractive" />
        <Script src="/js/wow.min.js" strategy="beforeInteractive" />
        <Script src="/js/gsap.min.js" strategy="beforeInteractive" />
        <Script src="/js/ScrollTrigger.min.js" strategy="beforeInteractive" />
        <Script src="/js/jquery.fancybox.min.js" strategy="beforeInteractive" />
        <Script src="/js/select-dropdown.js" strategy="lazyOnload" />
        <Script src="/js/custom.js" strategy="lazyOnload" />
      </body>
    </html>
  );
}
